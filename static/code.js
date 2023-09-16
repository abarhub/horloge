
console.log('test1');
console.log('test2');


function envoyer() {
    console.log('test3');

    var checkedValue = document.querySelector('input[name="action"]:checked').value;
    console.log('valeur',checkedValue);
    if(checkedValue) {
        fetch("/api/action/" + checkedValue)
            .then(response => {
                // indicates whether the response is successful (status code 200-299) or not
                // if (!response.ok) {
                //   throw new Error(`Request failed with status ${reponse.status}`)
                // }
                // return response.json()
                console.log('response:', response)
            })
            .then(data => {
                //console.log(data.count)
                //console.log(data.products)
            })
            .catch(error => console.error(error))
    }
}
