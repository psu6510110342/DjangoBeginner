const subform = document.querySelector('.sub-form')

function foodSet(event){
    const checkFoodSet = document.querySelectorAll('input[name="food_set"]:checked');
    if (checkFoodSet.length === 0) {
        event.preventDefault();
        alert('plese pick one oder')
    }
}

if (!!subform) {
    subform.addEventListener('submit', foodSet);
}