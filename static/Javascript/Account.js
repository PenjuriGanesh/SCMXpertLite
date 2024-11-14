function validateEmail() {
    const email = document.getElementById('account_email').value;
    const emailStatus = document.getElementById('email-status');
    
    // Simple email format validation
    const emailPattern = /^[a-zA-Z0-9._-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,6}$/;
    
    if (email.match(emailPattern)) {
      emailStatus.textContent = "Email is valid.";
      emailStatus.style.color = "green";
    } else {
      emailStatus.textContent = "Email is not valid.";
      emailStatus.style.color = "red";
    }
  }
  
  function sendVerification() {
    // Simulating email verification request (you'd handle this on the server)
    const emailStatus = document.getElementById('email-status');
    emailStatus.textContent = "Verification email sent! Please check your inbox.";
    emailStatus.style.color = "blue";
  }
  