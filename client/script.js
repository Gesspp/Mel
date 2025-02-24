const btn = document.querySelector('.button');
btn.addEventListener('click', () => eel.run_assistant());

const main = document.querySelector('main');
const settings = document.querySelector('.settings');
const settings_btn = document.querySelector('.settings-btn');

const add_program = document.querySelector('.add-program');
const add_program_modal = document.querySelector('.add-program-modal');
const close_program_button = document.querySelector('.close-program-button');
const add_new_program = document.querySelector('.add-new-program');
const edit_program = document.querySelector('.edit-program');
const edit_site = document.querySelector('.edit-site')

const add_new_site = document.querySelector('.add-new-site');
const add_site_modal = document.querySelector('.add-site-modal');
const add_site = document.querySelector('.add-site');
const close_site_button = document.querySelector('.close-site-button');

const add_new_scommand = document.querySelector('.add-new-scommand');
const add_scommand_modal = document.querySelector('.add-scommand-modal');
const add_scommand = document.querySelector('.add-scommand');
const close_scommand_button = document.querySelector('.close-scommand-button');
const subcommands_list = document.querySelector('.subcommands');
const add_subcommand = document.querySelector('.add-new-subcommand');

const volume_slider = document.querySelector('.volume-slider');

let old_program_name = ''; 



async function get_settings() {
    let settings = await eel.get_settings()();
    return settings
} 

volume_slider.addEventListener('input', function(e) {
    eel.set_volume(e.currentTarget.value / 100)();
})

add_program.addEventListener('click', () => {
    add_program_modal.classList.remove('hidden');
    edit_program.classList.add('hidden');
    add_new_program.classList.remove('hidden');
})

add_site.addEventListener('click', () => {
    add_site_modal.classList.remove('hidden');
    edit_site.classList.add('hidden');
    add_new_site.classList.remove('hidden');
})

add_scommand.addEventListener('click', () => {
    add_scommand_modal.classList.remove('hidden');
})

edit_program.addEventListener('click', () => {
    let program_name = document.querySelector('.new-program-name').value;
    let program_path = document.querySelector('.new-program-path').value;
    eel.edit_program(old_program_name, program_name, program_path);
    add_program_modal.classList.add('hidden');
    renderSettings();
})

edit_site.addEventListener('click', () => {
    let site_name = document.querySelector('.new-site-name').value;
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

add_new_scommand.addEventListener('click', () => {
    let scommand_name = document.querySelector('.new-scommand-name').value;
    let subcommands = [];
    const subcommands_list = Array.from(document.querySelectorAll('.subcommands>div'));
    for(let i = 0; i < subcommands_list.length; i++){
        const subcommand = subcommands_list[i].querySelector('.subcommand-select').value;
        const value = (subcommand === "открой" || subcommand === "закрой" ) ? subcommands_list[i].querySelector('.program-select').value : subcommands_list[i].querySelector('.subcommand-entry').value;
        subcommands.push(`${subcommand} ${value}`);
    }
    console.log(subcommands);
    eel.add_scommand(scommand_name, subcommands);
    add_scommand_modal.classList.add('hidden');
    renderSettings();
})

close_program_button.addEventListener('click', () => {
    add_program_modal.classList.add('hidden');
})

close_site_button.addEventListener('click', () => {
    add_site_modal.classList.add('hidden');
})

close_scommand_button.addEventListener('click', () => {
    add_scommand_modal.classList.add('hidden');
})


const subcommand_types = [
    "документ",
    "открой",
    "закрой",
    "выключи",
    "создай папку",
    "громкость",
    "загугли",
    "найди"
];

const subcommand_args = [];

const show_subcommand_args = (e) => {
    e.target.parentElement.querySelector('.program-select').classList.remove('hidden');
    e.target.parentElement.querySelector('.subcommand-entry').classList.add('hidden');
}
const hide_subcommand_args = (e) => {
    e.target.parentElement.querySelector('.program-select').classList.add('hidden');
    e.target.parentElement.querySelector('.subcommand-entry').classList.remove('hidden');
}

add_subcommand.addEventListener('click', () => {
    const subcommand = document.createElement('div');
    const program_select = document.createElement('select');
    const subcommand_select = document.createElement('select');
    subcommand_select.classList.add('subcommand-select');
    for(let i = 0; i < subcommand_types.length; i++){
        const option = document.createElement('option');
        option.value = subcommand_types[i];
        option.innerHTML = subcommand_types[i];
        subcommand_select.appendChild(option);
    }
    program_select.classList.add('hidden');
    program_select.classList.add('program-select');
    for(let i = 0; i < subcommand_args.length; i++){
        const option = document.createElement('option');
        option.value = subcommand_args[i];
        option.innerHTML = subcommand_args[i];
        program_select.appendChild(option);
    }
    const subcommand_entry = document.createElement('input');
    subcommand_entry.classList.add('subcommand-entry');
    subcommand_entry.setAttribute('placeholder', 'Введите название');
    
    subcommand.appendChild(subcommand_select);
    subcommand.appendChild(subcommand_entry);
    subcommand.appendChild(program_select);
    add_scommand_modal.querySelector('.subcommands').appendChild(subcommand);
    subcommand_select.addEventListener('change', function(e) {
        if (e.target.value == "открой" || e.target.value == "закрой") {
            show_subcommand_args(e);
        }
        else {
            hide_subcommand_args(e);
        }
    })
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
                        <div class="change-icon change-program"><img src="images/pen.png" /></div>
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
                        <div class="change-icon change-site"><img src="images/pen.png" /></div>
                        <div class="delete-icon delete-site"><img src="images/bin.png" /></div>
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
                        <div class="change-icon change-scommand"><img src="images/pen.png" /></div>
                        <div class="delete-icon delete-scommand"><img src="images/bin.png" /></div>
                    </div>
                </div>
            `;
            document.querySelector('.settings-scommands-list').appendChild(div);
            
        }
        for(let program in settings_info.programs){
            subcommand_args.push(program);
        }
        for(let sites in settings_info.sites){
            subcommand_args.push(sites);
        }
        const delete_program_buttons = document.querySelectorAll('.delete-program');
        const delete_site_button = document.querySelectorAll('.delete-site');
        const delete_scommand_button = document.querySelectorAll('.delete-scommand');
        if(delete_program_buttons){
            delete_program_buttons.forEach(delete_program => delete_program.addEventListener('click', () => {
                const program_name = delete_program.closest('.settings-programs-item').querySelector('.program-name').textContent;
                console.log("Удаляю программу", program_name);
                eel.delete_program(program_name);
                renderSettings();
            }));
        }
        if(delete_site_button){
            delete_site_button.forEach(delete_site => delete_site.addEventListener('click', () => {
                const site_name = delete_site.closest('.settings-sites-item').querySelector('.site-name').textContent;
                console.log("Удаляю сайт", site_name);
                eel.delete_site(site_name);
                renderSettings();
            }));
        }
        if(delete_scommand_button){
            delete_scommand_button.forEach(delete_scommand => delete_scommand.addEventListener('click', () => {
                const scommand_name = delete_scommand.closest('.settings-scommands-item').querySelector('.scommand-name').textContent;
                console.log("Удаляю суперкоманду", scommand_name);
                eel.delete_scommand(scommand_name); //нет двойных скобок потому что не нужен результат выполнения
                renderSettings();
            }));
        }
        const change_program_button = document.querySelectorAll('.change-program');
        const change_site_button = document.querySelectorAll('.change-site');
        const change_scommand_button = document.querySelectorAll('.change-scommand');
        if(change_program_button){
            change_program_button.forEach(change_program => change_program.addEventListener('click', () => {
                const program_name = change_program.closest('.settings-programs-item').querySelector('.program-name').textContent;
                document.querySelector('.new-program-name').value = program_name;
                document.querySelector('.new-program-path').value = settings_info.programs[program_name];
                old_program_name = program_name;
                add_program_modal.classList.remove('hidden');
                edit_program.classList.remove('hidden');
                add_new_program.classList.add('hidden');
            }));
        }
        if(change_site_button){
            change_site_button.forEach(change_site => change_site.addEventListener('click', () => {
                const site_name = change_site.closest('.settings-sites-item').querySelector('.site-name').textContent;
                document.querySelector('.new-site-name').value = site_name;
                document.querySelector('.URL_input').value = settings_info.sites[site_name];
                old_site_name = site_name;
                add_site_modal.classList.remove('hidden');
                edit_site.classList.remove('hidden');
                add_new_site.classList.add('hidden');
            }));
        }
        if(change_scommand_button){
            change_scommand_button.forEach(change_scommand => change_scommand.addEventListener('click', () => {
                const scommand_name = change_scommand.closest('.settings-scommands-item').querySelector('.scommand-name').textContent;
                document.querySelector('.new-scommand-name').value = scommand_name;
                old_scommand_name = scommand_name;
                add_scommand_modal.classList.remove('hidden');
                edit_scommand.classList.remove('hidden');
                add_new_scommand.classList.add('hidden');
            }));
        }
    });
}

renderSettings();

settings_btn.addEventListener('click', () => {
    main.classList.toggle('hidden');
    settings.classList.toggle('hidden');
});