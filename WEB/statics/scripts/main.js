
/* -- SCRIPTS --------------------------------------------------------------- */

document.addEventListener('DOMContentLoaded', () => {

    /** Comportamiento del SIDEBAR */
    const toggleButton = document.getElementById('toggle-main-sidebar');
    const sidebarContainer = document.querySelector('.main-sidebar-container');
    // const mainContent = document.querySelector('.main-content');

    if (toggleButton && sidebarContainer) {
        toggleButton.addEventListener('click', () => {
            sidebarContainer.classList.toggle('is-open');
        });
    }
});

/* -------------------------------------------------------------------------- */