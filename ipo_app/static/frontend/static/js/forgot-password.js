$(document).ready(function() {
    const form = $('#forgotPasswordForm');
    const emailInput = $('#email');
    const submitButton = $('.reset-button');

    // Form submission
    form.on('submit', function(e) {
        e.preventDefault();
        
        if (validateEmail(emailInput.val())) {
            // Verify reCAPTCHA
            const recaptchaResponse = grecaptcha.getResponse();
            if (!recaptchaResponse) {
                Swal.fire({
                    icon: 'error',
                    title: 'Verification Required',
                    text: 'Please complete the reCAPTCHA verification',
                    confirmButtonColor: '#6366f1'
                });
                return;
            }

            // Show loading state
            submitButton.prop('disabled', true)
                .addClass('loading')
                .html('<span class="spinner"></span><span class="button-text">Sending...</span>');

            // Send reset password request
            $.ajax({
                url: '/api/forgot-password',
                method: 'POST',
                data: {
                    email: emailInput.val(),
                    recaptchaResponse: recaptchaResponse
                },
                success: function(response) {
                    Swal.fire({
                        icon: 'success',
                        title: 'Email Sent!',
                        text: 'Please check your email for password reset instructions.',
                        confirmButtonColor: '#6366f1'
                    }).then(() => {
                        window.location.href = './login.html';
                    });
                },
                error: function(xhr) {
                    const error = xhr.responseJSON?.message || 'Something went wrong. Please try again.';
                    Swal.fire({
                        icon: 'error',
                        title: 'Error',
                        text: error,
                        confirmButtonColor: '#6366f1'
                    });
                    submitButton.prop('disabled', false)
                        .removeClass('loading')
                        .html('<span class="button-text">Password Reset</span>');
                    grecaptcha.reset();
                }
            });
        }
    });

    // Email validation
    function validateEmail(email) {
        const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
        if (!emailRegex.test(email)) {
            Swal.fire({
                icon: 'error',
                title: 'Invalid Email',
                text: 'Please enter a valid email address',
                confirmButtonColor: '#6366f1'
            });
            return false;
        }
        return true;
    }

    // Real-time email validation
    emailInput.on('blur', function() {
        const email = $(this).val();
        if (email && !validateEmail(email)) {
            $(this).addClass('error');
        } else {
            $(this).removeClass('error');
        }
    });

    // Back to login link handler
    $('.back-to-login a').on('click', function(e) {
        e.preventDefault();
        window.location.href = './login.html';
    });
}); 