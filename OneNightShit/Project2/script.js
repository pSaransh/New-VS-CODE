
const addBtn = document.getElementById('add');

addBtn.addEventListener('click', () => {
    addNewNote();
});


function addNewNote(){
    const note = document.createElement('div');
    note.classList.add('note');
    note.innerHTML = `
    <div class="notes">
        <div class="tools">
            <button class="edit"><i class="fas fa-edit"></i></button>
            <button class="delete"><i class="fas fa-trash-alt"></i></button>
        </div>
        <div class="main hidden"></div> 
        <textarea></textarea>
    </div>
    `;
    const editBtn = note.querySelector('.edit');
    const deletetBtn = note.querySelector('.delete');
    const main = note.querySelector('.main');
    const textArea = note.querySelector('textarea');

    editBtn.addEventListener('click',() => {
        note.classList.toggle('hidden');
        main.classList.toggle('hidden');
        textArea.classList.toggle('hidden');
    });

    deletetBtn.addEventListener('click',() => {
        note.remove();
    });

    textArea.addEventListener('input',(e) => {
        const { value } = e.target;
        main.innerHTML = marked.parse(value);
    });

    document.body.appendChild(note);
} 
