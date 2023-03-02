// menu
const menuBtn = document.getElementById('menu-btn')
const closeBtn = document.getElementById('close-btn')
const menu = document.getElementById('menu')

menuBtn.addEventListener('click',()=>{
    menu.classList.add('active')
})
closeBtn.addEventListener('click',()=>{
    menu.classList.remove('active')
})
// product add and remove
const addBtns = document.querySelectorAll('.add')
const removeBtns = document.querySelectorAll('.remove')
const quantityText = document.querySelectorAll('.quantity')
const totalPrices = document.querySelectorAll('.total')
const prices = document.querySelectorAll('.price')
const productBill = document.getElementById('product-total')
const payable = document.getElementById('all')



quantityText.forEach(quantity=>{
    quantity.innerHTML = 1
})

totalPrices.forEach((price,idx)=>{
    price.innerHTML = prices[idx].innerHTML
})

updateBill()
addBtns.forEach((addBtn,idx)=>{
    addBtn.addEventListener('click',()=>{
        quantityText[idx].innerHTML++
        calcTotal(idx,quantityText[idx])
        updateBill()
    })

})
removeBtns.forEach((removeBtn,idx)=>{
    removeBtn.addEventListener('click',()=>{
        if (quantityText[idx].innerHTML<2){
            quantityText[idx].innerHTML = 1
        }
        else{
            quantityText[idx].innerHTML--
        }
        calcTotal(idx,quantityText[idx])
        updateBill()  
    })
})

function calcTotal(index,price){
    totalPrices[index].innerHTML = price.innerHTML*prices[index].innerHTML


}

function updateBill(){
    let productTotal = 0
    totalPrices.forEach(total=>{
        productTotal += Number(total.innerHTML)
        
    })
    console.log(productTotal)
    console.log(productBill)
    productBill.innerText = productTotal
    payable.innerText = productTotal+50000
}




