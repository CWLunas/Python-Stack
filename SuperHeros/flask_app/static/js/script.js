console.log('hello from javascript')



function search(e){
    e.preventDefault(); 
    let searchForm= document.getElementById('searchForm');
    let form= new FormData(searchForm);
    fetch('http://localhost:5000/searching',{method:'POST',body:form})
        .then(res=> res.json())
        .then(data=> {
            console.log(data['results'][0]);
            for(let i=0; i<data['results'].length;i++){
                let main_div= document.getElementById('main')

                let card_div = document.createElement('div')
                card_div.className= "card"
                card_div.style="width: 18rem;"
    
                let card_img = document.createElement('img')
                card_img.className="card-img-top"
                card_img.src= data['results'][i]['image']['url']
    
                let card_body= document.createElement('div')
                card_body.className="card-body"
    
                let card_title= document.createElement('h2')
                card_title.className="card-title"
                card_title.innerText= data['results'][i]['name']
    
                let card_text= document.createElement('p')
                card_text.className= "card-text"
                card_text.innerText=data['results'][i]['biography']['first-appearance']
    
                let card_link= document.createElement('a')
                card_link.className= "btn btn-primary"
                card_link.innerText="add to favorites"
                hero_id=data['results'][i]['id']
                
                card_link.href=`/dashboard/1/${hero_id}` //this is called template literal

                card_body.appendChild(card_link)
                card_body.appendChild(card_title)
                card_body.appendChild(card_text)
                card_div.appendChild(card_img)
                card_div.appendChild(card_body)
                main_div.appendChild(card_div)

            }


        })
}
