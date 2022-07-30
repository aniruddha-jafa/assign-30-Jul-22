import { useState, useCallback } from 'react'
import { Box, Grid, GridItem, VStack, Button, Container, Input } from '@chakra-ui/react'

import { LineChart, Line, CartesianGrid, XAxis, YAxis } from 'recharts'

import calculate from './calculate'

// const data = [
//   { name: 'Page A', uv: 400, pv: 2400, amt: 2400 },
//   { name: 'Page B', uv: 200, pv: 2400, amt: 2400 },
//   { name: 'Page C', uv: 100, pv: 2400, amt: 2400 },
//   { name: 'Page D', uv: 600, pv: 2400, amt: 2400 },
//   { name: 'Page E', uv: -30, pv: 2400, amt: 2400 }
// ]

const Chart = ({ data }) => {

  return (
    <Box mt={16}>
    <LineChart width={600} height={300} data={data}>
      <Line type="monotone" dataKey="y" stroke="#8884d8" />
      <CartesianGrid stroke="#ccc" />
      <XAxis />
      <YAxis />
    </LineChart>
    </Box>
  )
}

export default function Home() {
  const [input, setInput] = useState('')
  const [data, setData] = useState([])

  const handleChange = useCallback((e) => {
    e.preventDefault()
    setInput(e.target.value)
  }, [])

  const handleSubmit = useCallback((e) => {
    e.preventDefault()
    try {
      const results = calculate(input)
      setData(results)
    } catch (err) {
      alert('Error: ', err)
    }
  }, [input])
  return (
    <>
      <Grid templateRows="1fr 200px" minH='100vh'>
        <GridItem>
          <VStack h='100%' py={16}>
            <Container display='flex' flexDirection='column' justifyContent={'center'} alignItems='center' gap={4} as='form'>
              <Input onChange={handleChange} placeholder='Type here' w='100%' />
              <Button type='submit' onClick={handleSubmit} colorScheme={'blue'}>
                Go
              </Button>
              <Chart data={data}  />
            </Container>
          </VStack>
        </GridItem>
        <GridItem as='footer' bgColor='gray.200' p={8}>
        </GridItem>
      </Grid>
    </>
  )
}
