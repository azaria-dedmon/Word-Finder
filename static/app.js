const form = document.querySelector('#form')
// const input = $("#guess").val();
let score = 0
let scoreNumber = document.querySelector('h1')
let btn = document.querySelector('#btn')

form.addEventListener('submit', async (e) => {
    e.preventDefault()

    const word = document.getElementById('guess').value
    let message = document.querySelector('h3')

    let res = await axios.get('/check-answer', {params: {word: word}})
    let dataResult = res.data.result

 
    if(dataResult === "not-word") {
        message.innerText = 'That word does not exist.'
    } else if (dataResult === "not-on-board") {
        message.innerText = 'Good guess, but is not on board.'
    } else if (dataResult === "ok") {
        score = score + word.length
        message.innerText = 'Good eyes!'
    }
    scoreNumber.innerText = score
    
    
    setTimeout(function() {
        btn.disabled = true
        post()
    }, 60000)

    const post = async () => {
    const res = await axios.post('/num-plays', {
        score: score
    })
    console.log(res.data)
    }
})

