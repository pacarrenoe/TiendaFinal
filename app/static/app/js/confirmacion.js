function confirmarEliminacion(codigoproducto) {
    Swal.fire({
        title: '¿Estas seguro de esto?',
        text: "Ya no podras volver a recuperarlo",
        icon: '¡ALTO!',
        showCancelButton: true,
        confirmButtonColor: '#3085d6',
        cancelButtonColor: '#d33',
        confirmButtonText: 'Si, eliminar',
        cancelButtonText: 'Cancelar',
      }).then((result) => {
        if (result.value) {
          window.location.href="/usuario_eliminar/"+codigoproducto;
        }
      })
}