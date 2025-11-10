
/* -- SCRIPTS --------------------------------------------------------------- */

document.addEventListener('DOMContentLoaded', () => {
    setTimeout(() => {
        const resultado = document.getElementById('resultado');

        if (resultado) {
            resultado.scrollIntoView({ behavior: 'smooth', block: 'center' });
        }
    }, 300);
});

/* -------------------------------------------------------------------------- */