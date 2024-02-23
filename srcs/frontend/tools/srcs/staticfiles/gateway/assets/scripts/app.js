
const signin = document.createElement('main');
signin.className = 'form-signin w-100 m-auto';

const login = document.createElement('form');

const idDiv = document.createElement('div');
idDiv.className = 'form-floating';

const idInput = document.createElement('input');
idInput.className = 'form-control';
idInput.setAttribute('type', 'email');

const pwDiv = document.createElement('div');
pwDiv.className = 'form-floating';

const pwInput = document.createElement('input');
pwInput.className = 'form-control';
pwInput.setAttribute('type', 'float');

const submitButton = document.createElement('button');
submitButton.className = 'btn btn-primary w-100 py-2'
submitButton.setAttribute('type', 'submit')
submitButton.textContent = 'Sign in'

class app {
	static init() {
		const body = document.querySelector('body');
		body.className = 'd-flex align-items-center py-4 bg-body-tertiary';
		const application = document.querySelector('#app');
		idDiv.append(idInput);
		login.append(idDiv);
		pwDiv.append(pwInput);
		login.append(pwDiv);
		login.append(submitButton);
		signin.append(login);
		application.append(signin);
	}
}

app.init();