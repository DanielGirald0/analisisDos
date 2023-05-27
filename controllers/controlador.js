let boton = document.getElementById("btngenerarreporte")
boton.addEventListener("click", function(evento){
    evento.preventDefault()
    let contenedor=document.getElementById("contenedor")
    contenedor.classList.remove("d-none")

    let nombreusuario=document.getElementById("nombre").value
    let mensaje=document.getElementById("mensaje")

    mensaje.textContent=`Apreciado usuario ${nombreusuario}, hemos generado su eporte: `
})