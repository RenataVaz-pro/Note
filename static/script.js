function enableEditing(notaId) {
    document.getElementById('titulo-' + notaId).removeAttribute('readonly');
    document.getElementById('descricao-' + notaId).removeAttribute('readonly');
    document.getElementById('save-' + notaId).style.display = 'inline';
}
function toggleSidebar() {
    const sidebar = document.getElementById("sidebar");
    if (sidebar.style.left === "0px") {
        sidebar.style.left = "-300px"; 
    } else {
        sidebar.style.left = "0px";
    }
}
function toggleSidebar() {
    const sidebar = document.getElementById('sidebar');
    sidebar.classList.toggle('open');
}
function keepSidebarOpen() {
    localStorage.setItem('sidebarOpen', 'true');
}
window.onload = function() {
    const sidebar = document.getElementById('sidebar');
    if (localStorage.getItem('sidebarOpen') === 'true') {
        sidebar.classList.add('open');
    }
};

function toggleSidebar() {
    const sidebar = document.getElementById('sidebar');
    sidebar.classList.toggle('open');
    localStorage.setItem('sidebarOpen', sidebar.classList.contains('open'));
}

document.querySelectorAll('.form-deletar').forEach(form => {
    form.addEventListener('submit', function(event) {
        event.preventDefault(); 
        const notaId = this.getAttribute('id').split('-')[2]; 
        const formData = new FormData(this);

        fetch(this.action, {
            method: 'POST',
            body: formData
        })
        .then(response => response.json())
        .then(data => {
            if (data.status === 'success') {
                const notaBox = document.querySelector(`#form-${notaId}`).closest('.nota-box');
                notaBox.remove();
            } else {
                console.error("Erro ao deletar a nota:", data);
            }
        })
        .catch(error => console.error("Erro na requisição:", error));
    });
});
