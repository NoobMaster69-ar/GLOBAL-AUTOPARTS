new Autocomplete('#autocomplete', {
    search: input => {
        const url = `/private/search/?search=${input}`;

        return new Promise(resolve => {
            if (input.length < 3) {
                return resolve([]);
            }

            document.getElementById('productDetails').classList.add('d-none');

            fetch(url)
                .then(response => response.json())
                .then(data => {
                    if (data.data.length < 1) {
                        showToast('warning', 'No se encontraron coincidencias');
                        return resolve([]);
                    } else {
                        resolve(data.data);
                    }
                });
        });
    },

    debounceTime: 1000,

    renderResult: (result, props) => {
        return `
            <li ${props}>
                <div class="wiki-title">
                    ${result.description}
                </div>
            </li>
        `;
    },

    getResultValue: result => result.description,

    onSubmit: result => {
        const url = `/private/search/?search=${result.id}`;
        fetch(url, {
            method: 'POST',
            headers: {
                'X-CSRFToken': getCsrfToken(),
                'Content-Type': 'application/x-www-form-urlencoded',
            },
            body: new URLSearchParams({
                search: result.id,
            })
        })
            .then(response => response.json())
            .then(data => {
                const productData = data.data;
                document.getElementById('productDetails').classList.remove('d-none');
                document.getElementById('productName').textContent = productData.description;
                document.getElementById('productQuality').textContent = productData.origin;
                document.getElementById('productPrice').textContent = productData.price;
                document.getElementById('productImage').src = productData.image;
            });
    }
});

document.getElementById('productImage').addEventListener('click', function () {
    const modalImage = document.getElementById('modalImage');
    modalImage.src = this.src;
    const imageModal = new bootstrap.Modal(document.getElementById('imageModal'));
    imageModal.show();
});