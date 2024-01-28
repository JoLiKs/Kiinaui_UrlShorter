 let myRandom = (a, b) => {
        return Math.round(Math.random() * (b - a) + a)
    }
let curR = myRandom(0, 255)
let curG = myRandom(0, 255)
let curB = myRandom(0, 255)
let nextR = myRandom(0, 255)
let nextG = myRandom(0, 255)
let nextB = myRandom(0, 255)
window.interval = setInterval(() => {
    if (curR === nextR && curG === nextG && curB === nextB) {
        nextR = myRandom(0, 255)
        nextG = myRandom(0, 255)
        nextB = myRandom(0, 255)
        console.log("NEW COLOR")
        console.log(nextR)
        console.log(nextG)
        console.log(nextB)
    }
    if (curR < nextR) {
        curR++
    }
    if (curR > nextR) {
        curR--
    }
    if (curG < nextG) {
        curG++
    }
    if (curG > nextG) {
        curG--
    }
    if (curB < nextB) {
        curB++
    }
    if (curB > nextB) {
        curB--
    }
    document.body.style.background = `rgb(${curR}, ${curG}, ${curB})`
}, 90)
