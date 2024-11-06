function loadData(event) {
    event.preventDefault() 
    const fileInput = document.getElementById('inputFile');
    const supplierSelect = document.getElementById('supplierSelect');
    
    if (fileInput.files.length === 0) {
        showToast('error', 'No se ha seleccionado ningún archivo');
        return;
    }
    
    const formData = new FormData();

    formData.append('file', fileInput.files[0]);
    formData.append('supplier', supplierSelect.value);

    fetch('/private/administration/', {
        method: 'POST',
        headers: {
            'X-CSRFToken': getCsrfToken()
        },
        body: formData,
    })
        .then(response => response.json())
        .then(data => {
            showToast(data.status, data.message);
        })
    .catch(error => {
        showToast('error', error);
    });
}

function eraseData() {
    fetch('/private/erase/', {
        method: 'POST',
        headers: {
            'X-CSRFToken': getCsrfToken()
        }
    })
    .then(response => response.json())
    .then(data => {
        showToast(data.status, data.message).then(() => {
            if (data.status === 'success') {
                window.location.reload();
            }
        });
    })
    .catch(error => {
        showToast('error', error);
    });
}