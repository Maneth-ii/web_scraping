let news = []
async function get_data(){
    try{
        await fetch('http://127.0.0.1:5000')
        // http://127.0.0.1:5000
        .then(res=>
            res.json())
            .then(data=>
                news = data );
                setToDocument()
        console.log(news)
    }
    catch(e){
    }
}
get_data()

const listParent = document.getElementById("news-list")

function setToDocument() {
    news.map((aNews) => {
        const li = document.createElement('li');
        li.innerHTML =
            `<h1>${aNews.Title}</h1>
            <p>${aNews.Description}</p>
            <img src=${aNews.Image}/>
            <a href=${aNews.Link}>Link</a>
            `;
        listParent.appendChild(li);
    });
}

setToDocument();