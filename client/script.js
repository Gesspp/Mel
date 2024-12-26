const btn = document.querySelector('.button');
btn.addEventListener('click', () => eel.run_assistant());

const main = document.querySelector('main');
const settings = document.querySelector('.settings');
const settings_btn = document.querySelector('.settings-btn');

const add_program = document.querySelector('.add-program');
const add_program_modal = document.querySelector('.add-program-modal');
const close_program_button = document.querySelector('.close-program-button');
const add_new_program = document.querySelector('.add-new-program');

const add_new_site = document.querySelector('.add-new-site');
const add_site_modal = document.querySelector('.add-site-modal');
const add_site = document.querySelector('.add-site');
const close_site_button = document.querySelector('.close-site-button');

const volume_slider = document.querySelector('.volume-slider');



async function get_settings() {
    let settings = await eel.get_settings()();
    return settings
} 

volume_slider.addEventListener('input', function(e) {
    eel.set_volume(e.currentTarget.value / 100)();
})

add_program.addEventListener('click', () => {
    add_program_modal.classList.remove('hidden');
})

add_site.addEventListener('click', () => {
    add_site_modal.classList.remove('hidden');
})

add_new_program.addEventListener('click', () => {
    let program_name = document.querySelector('.new-program-name').value;
    let program_path = document.querySelector('.new-program-path').value;
    eel.add_program(program_name, program_path);
    add_program_modal.classList.add('hidden');
    renderSettings();
})

add_new_site.addEventListener('click', () => {
    let site_name = document.querySelector('.new-site-name').value;
    let site_url = document.querySelector('.URL_input').value;
    eel.add_site(site_name, site_url);
    add_site_modal.classList.add('hidden');
    renderSettings();
})



close_program_button.addEventListener('click', () => {
    add_program_modal.classList.add('hidden');
})

close_site_button.addEventListener('click', () => {
    add_site_modal.classList.add('hidden');
})

const svgFolderIcon = `<svg version="1.1" id="Layer_1" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" x="0px" y="0px" viewBox="0 0 512 512" style="enable-background:new 0 0 512 512;" xml:space="preserve"><g><g><path d="M496,108.132H273.456l-72.584-71.256H0v87.256v35.488v299.496c0,8.808,7.2,16.008,16,16.008h480c8.8,0,16-7.2,16-16 V124.132C512,115.332,504.8,108.132,496,108.132z M32,68.868h155.792l39.984,39.256H32V68.868z M480,443.124H32V159.62v-19.488 h448V443.124z"/></g></g></svg>`;

const renderSettings = () => {
    document.querySelector('.settings-sites-list').innerHTML = '';
    document.querySelector('.settings-programs-list').innerHTML = '';
    document.querySelector('.settings-scommands-list').innerHTML = '';
    get_settings().then(settings_info => {
        for(let program in settings_info.programs){
            let div = document.createElement('div');
            div.innerHTML = `
                <div class="settings-programs-item">
                    <p class="program-name">${program}</p>
                    <div class="change-icon">${svgFolderIcon}</div>
                    <div class="icons">
                        <div class="change-icon"><img src="images/pen.png" /></div>
                        <div class="delete-icon delete-program"><img src="images/bin.png" /></div>
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
                        <div class="change-icon"><img src="images/pen.png" /></div>
                        <div class="delete-icon"><img src="images/bin.png" /></div>
                    </div>
                </div>
            `;
            document.querySelector('.settings-sites-list').appendChild(div);
        }
        for(let sc in settings_info.supercommands){
            let div = document.createElement('div');
            div.innerHTML = `
                <div class="settings-scommands-item">
                    <p class="scommand-name">${sc}</p>
                    <div class="icons">
                        <div class="change-icon"><img src="images/pen.png" /></div>
                        <div class="delete-icon"><img src="images/bin.png" /></div>
                    </div>
                </div>
            `;
            document.querySelector('.settings-scommands-list').appendChild(div);
        }
        const delete_program_buttons = document.querySelectorAll('.delete-program');
        if(delete_program_buttons){
            delete_program_buttons.forEach(delete_program => delete_program.addEventListener('click', () => {
                const program_name = delete_program.closest('.settings-programs-item').querySelector('.program-name').textContent;
                console.log("Удаляю программу", program_name);
                eel.delete_program(program_name);
                renderSettings();
            }));
        }
    });
}

renderSettings();

settings_btn.addEventListener('click', () => {
    main.classList.toggle('hidden');
    settings.classList.toggle('hidden');
});