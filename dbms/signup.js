let otpVerified = false; // Variable to track OTP verification status
let generatedOtp; // Store the generated OTP
let timerInterval; // Store the timer interval for cleanup

function showStep2() {
    document.getElementById('step1').style.display = 'none';
    document.getElementById('step2').style.display = 'block';
}

function sendOtp() {
    // Generate a random OTP
    generatedOtp = Math.floor(100000 + Math.random() * 900000); // 6-digit OTP
    alert(`Your OTP is: ${generatedOtp}`); // Simulate sending OTP

    // Enable the OTP input field
    document.getElementById('otp').disabled = false;
    startTimer(); // Start the countdown timer
}

function verifyOtp() {
    const otpInput = document.getElementById('otp').value;

    if (otpInput === generatedOtp) {
        otpVerified = true; // Mark OTP as verified
        alert("OTP Verified Successfully!");
        window.location.href = "index.html"; // Redirect to home page after clicking OK
    } else {
        document.getElementById('otpFeedback').textContent = "OTP is incorrect, please try again.";
    }
}

function startTimer() {
    let timeLeft = 120; // 2 minutes countdown
    const timerDisplay = document.getElementById('timer');
    const resendButton = document.getElementById('resendOtp');

    // Clear any existing timer
    clearInterval(timerInterval);
    
    timerInterval = setInterval(() => {
        timeLeft--;

        const minutes = Math.floor(timeLeft / 60);
        const seconds = timeLeft % 60;

        timerDisplay.textContent = `Time left: ${String(minutes).padStart(2, '0')}:${String(seconds).padStart(2, '0')}`;

        if (timeLeft <= 0) {
            clearInterval(timerInterval);
            timerDisplay.textContent = "Time's up!";
            resendButton.style.display = 'block'; // Show resend OTP button
        }
    }, 1000);
}
