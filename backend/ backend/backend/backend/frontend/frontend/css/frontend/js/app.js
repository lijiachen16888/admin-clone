document.getElementById('loginForm').addEventListener('submit', async function (e) {
  e.preventDefault();

  const username = document.getElementById('username').value.trim();
  const password = document.getElementById('password').value.trim();
  const messageEl = document.getElementById('message');

  if (!username || !password) {
    messageEl.textContent = '用户名和密码不能为空';
    return;
  }

  try {
    const response = await fetch('https://your-backend-url/api/login', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json'
      },
      body: JSON.stringify({ username, password })
    });

    const result = await response.json();

    if (result.success) {
      // 登录成功，跳转到后台首页
      window.location.href = 'dashboard.html';
    } else {
      messageEl.textContent = result.message || '登录失败';
    }
  } catch (error) {
    messageEl.textContent = '网络错误，请稍后重试';
  }
});
