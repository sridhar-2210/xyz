let generatedOtp = ""; // Variable to store the generated OTP
let timerInterval; // Variable to store timer interval

function sendOtp() {
    const phone = document.getElementById('phone').value;
    
    // Generate a random 6-digit OTP
    generatedOtp = Math.floor(100000 + Math.random() * 900000).toString();
    
    // Logic to send OTP to the provided phone number
    alert(`OTP sent to ${phone}. Please check your messages.`);

    // Show the OTP modal for user to enter OTP
    $('#otpModal').modal('show'); 

    startTimer(); // Start timer for OTP verification
}

function verifyOtp() {
    const otpInput = document.getElementById('otp').value;

    if (otpInput === generatedOtp) {
        otpVerified = true; // Mark OTP as verified
        alert("OTP Verified Successfully!");
        $('#otpModal').modal('hide'); // Hide the OTP modal
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
