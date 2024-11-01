document.querySelectorAll('.gallery-img').forEach(img =>{
    img.addEventListener('click', function(){
        document.getElementById('modal-photo').src = this.src
    })
})