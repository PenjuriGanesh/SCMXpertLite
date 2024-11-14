(function(){
  const fonts = ["cursive", "sans-serif", "serif", "monospace"];
  let captchaValue = "";

  // Function to generate the captcha value
  function generateCaptcha() {
    let value = btoa(Math.random() * 1000000000); // Base64 encode the random number
    value = value.substr(0, 5 + Math.random() * 5); // Truncate the string to 5-10 characters
    captchaValue = value;
  }

  // Function to set the captcha value in the preview area
  function setCaptcha() {
    let html = captchaValue.split("").map((char) => {
      const rotate = -20 + Math.trunc(Math.random() * 30); // Random rotation for each character
      const font = Math.trunc(Math.random() * fonts.length); // Random font family
      return `<span
        style="
          transform:rotate(${rotate}deg);
          font-family:${fonts[font]}";
      >${char}</span>`;
    }).join("");
    
    // Inject the captcha HTML into the preview div
    document.querySelector(".login-form .captcha .preview").innerHTML = html;
  }

  // Function to initialize captcha
  function initCaptcha() {
    // Add event listener for the captcha refresh button
    document.querySelector(".login-form .captcha .captcha-refresh").addEventListener("click", function() {
      generateCaptcha();
      setCaptcha();
    });

    // Generate and display the initial captcha
    generateCaptcha();
    setCaptcha();
  }

  // Initialize the captcha when the page loads
  initCaptcha();

  // Add event listener for the login button
  document.querySelector(".login-form #login-btn").addEventListener("click", function() {
    let inputCaptchaValue = document.querySelector(".login-form .captcha input").value;
    
    // Check if the inputted captcha matches the generated captcha
    if(inputCaptchaValue === captchaValue) {
      // Show the success message
      showLoginSuccess();

      // After successful captcha validation, redirect to /Dashboard after 2 seconds
      setTimeout(function() {
        window.location.href = "/Dashboard";
      }, 2000);  // 2 seconds delay
    } else {
      swal("Invalid captcha"); // Alert if captcha is incorrect
    }
  });

  // Function to display the login success message
  function showLoginSuccess() {
    const successMessage = document.createElement("div");
    successMessage.classList.add("login-success-message");
    successMessage.innerHTML = "Logging In!";
    
    // Add the success message to the body
    document.body.appendChild(successMessage);

    // Show the success message (no animation)
    setTimeout(() => {
      successMessage.classList.add("show");
    }, 100);

    // Remove the success message after 2 seconds
    setTimeout(() => {
      successMessage.remove();
    }, 2000);  // Remove after 2 seconds
  }
})();
