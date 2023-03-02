const deleteBtn = document.querySelectorAll('.delete-btn')
const deleteMsgBox = document.getElementById('delete-msgbox')
const cmsOverlay = document.getElementById('cms-overlay')
const deleteCancelBtn = document.getElementById('delete-cancel-btn')

deleteBtn.forEach(btn=>{
    btn.addEventListener('click',()=>{
        cmsOverlay.classList.add('cms-overlay-active')
        deleteMsgBox.classList.add('delete-msgbox-active')
    })
})
deleteCancelBtn.addEventListener('click',()=>{
    cmsOverlay.classList.remove('cms-overlay-active')
    deleteMsgBox.classList.remove('delete-msgbox-active')
})