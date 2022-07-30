import  { parse } from 'mathjs'

const BEGIN = -100, END = 100

/**
 * 
 * @param {string} expr 
 * @returns {number[]}
 */
function calculate(expr) {
    const eq = parse(expr)
    let results = []
    for (let i = BEGIN; i < END; i = i + 10) {
        const val = eq.evaluate({ x: i })
        results.push({ x: i, y: val })
    }
    return results
}


export default calculate