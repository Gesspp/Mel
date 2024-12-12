const btn = document.querySelector('.button');
btn.addEventListener('click', () => eel.run_assistant());

const main = document.querySelector('main');
const settings = document.querySelector('.settings');
const add_program = document.querySelector('.add-program');
const add_program_modal = document.querySelector('.add-program-modal');
const settings_btn = document.querySelector('.settings-btn');
const close_modal_button = document.querySelector('.close-modal-button');

async function get_settings() {
    let settings = await eel.get_settings()();
    return settings
} 

add_program.addEventListener('click', () => {
    add_program_modal.classList.remove('hidden');
})

close_modal_button.addEventListener('click', () => {
    add_program_modal.classList.add('hidden');
})
const svgFolderIcon = `<svg version="1.1" id="Layer_1" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" x="0px" y="0px" viewBox="0 0 512 512" style="enable-background:new 0 0 512 512;" xml:space="preserve"><g><g><path d="M496,108.132H273.456l-72.584-71.256H0v87.256v35.488v299.496c0,8.808,7.2,16.008,16,16.008h480c8.8,0,16-7.2,16-16 V124.132C512,115.332,504.8,108.132,496,108.132z M32,68.868h155.792l39.984,39.256H32V68.868z M480,443.124H32V159.62v-19.488 h448V443.124z"/></g></g></svg>`;


get_settings().then(settings_info => {
    for(let program in settings_info.programs){
        let div = document.createElement('div');
        div.innerHTML = `
            <div class="settings-programs-item">
                <p class="program-name">${program}</p>
                <div class="change-icon">${svgFolderIcon}</div>
                <div class="icons">
                    <div class="delete-icon"><img src="images/pen.png" /></div>
                    <div class="change-icon"><img src="images/bin.png" /></div>
                </div>
            </div>
        `;
        document.querySelector('.settings-programs-list').appendChild(div);
    }
    for(let site in settings_info.sites){
        let div = document.createElement('div');
        div.innerHTML = `
            <div class="settings-sites-item">
                <p class="site-name">${site}</p>
                <div class="icons">
                    <div class="delete-icon"><img src="images/pen.png" /></div>
                    <div class="change-icon"><img src="images/bin.png" /></div>
                </div>
            </div>
        `;
        document.querySelector('.settings-sites-list').appendChild(div);
    }
});

settings_btn.addEventListener('click', () => {
    main.classList.toggle('hidden');
    settings.classList.toggle('hidden');
});