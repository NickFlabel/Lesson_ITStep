
        function loadAuthors() {
            const url = 'http://127.0.0.1:8000/api/authors/';

            fetch(url)
                .then(response => response.json())
                .then(data => {
                    const authorsList = document.getElementById('authorsList');
                    authorList.innerHTML = '';

                    data.forEach(author => {
                        const listItem = document.createElement('li');
                        listItem.className = 'list-group-item';

                        const authorId = document.createElement('span');
                        authorId.className = 'mr-2';
                        authorId.textContent = `ID: ${author.id}`;

                        const authorName = document.createElement('span');
                        authorName.className = 'mr-2';
                        authorName.textContent = `ID: ${author.name}`;

                        listItem.appendChild(authorId);
                        listItem.appendChild(authorName);

                        authorList.appendChild(listItem);
                });
            })
            .catch(error => {
                console.log(error);
            });
        })}

        const loadAuthorsButton = document.getElementById('loadAuthorsButton');
        loadAuthorsButton.addEventListener('click', loadAuthors);
