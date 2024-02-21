const signin = document.createElement('main');

	const login = document.createElement('form');

		const idDiv = document.createElement('div');

			const idInput = document.createElement('input');

		const pwDiv = document.createElement('div');

			const pwInput = document.createElement('input');

		const submitButton = document.createElement('button');

class app {
	static init() {
		const body = document.querySelector('body');
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