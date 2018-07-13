const nomeInput = document.querySelector('input[name=nome]');
const slugInput = document.querySelector('input[name=slug]');

const slugify = (val) => {
    return val.toString().toLowerCase().trim()
        .replace(/&/g, '-e-')
        .replace(/[\s\W-]+/g, '-')
};

nomeInput.addEventListener('keyup', (e)=>{
    slugInput.setAttribute('value', slugify(nomeInput.value));
});