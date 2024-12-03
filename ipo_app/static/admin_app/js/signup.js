$(document).ready(function() {
    const form = $('form');
    const inputs = $('input');
    const passwordInput = $('#password');
    const togglePassword = $('#togglePassword');
    const submitButton = $('.signup-button');
    
    // Password strength indicators
    passwordInput.on('input', function() {
        const password = $(this).val();
        const strength = checkPasswordStrength(password);
        updatePasswordStrength(strength);
    });

    // Show/Hide password
    togglePassword.on('click', function() {
        const type = passwordInput.attr('type') === 'password' ? 'text' : 'password';
        passwordInput.attr('type', type);
        $(this).toggleClass('fa-eye fa-eye-slash');
    });

    // Real-time validation
    inputs.on('blur', function() {
        validateField($(this));
    });

    // Form submission
    form.on('submit', function(e) {
        e.preventDefault();
        
        if (validateForm()) {
            const formData = {
                name: $('#name').val(),
                email: $('#email').val(),
                password: $('#password').val()
            };

            submitButton.prop('disabled', true).html('<span class="spinner"></span> Signing up...');

            // Simulate API call
            setTimeout(() => {
                $.ajax({
                    url: '/api/signup',
                    method: 'POST',
                    data: formData,
                    success: function(response) {
                        Swal.fire({
                            icon: 'success',
                            title: 'Success!',
                            text: 'Your account has been created successfully.',
                            showConfirmButton: false,
                            timer: 2000
                        }).then(() => {
                            window.location.href = '/dashboard';
                        });
                    },
                    error: function(xhr) {
                        const error = xhr.responseJSON?.message || 'Something went wrong. Please try again.';
                        Swal.fire({
                            icon: 'error',
                            title: 'Oops...',
                            text: error
                        });
                        submitButton.prop('disabled', false).text('Sign up');
                    }
                });
            }, 1500);
        }
    });

    // Validation functions
    function validateField(field) {
        const value = field.val();
        const name = field.attr('name');
        let isValid = true;
        let message = '';

        switch(name) {
            case 'name':
                if (value.length < 2) {
                    isValid = false;
                    message = 'Name must be at least 2 characters long';
                }
                break;
            case 'email':
                const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
                if (!emailRegex.test(value)) {
                    isValid = false;
                    message = 'Please enter a valid email address';
                }
                break;
            case 'password':
                if (value.length < 8) {
                    isValid = false;
                    message = 'Password must be at least 8 characters long';
                }
                break;
        }

        updateFieldStatus(field, isValid, message);
        return isValid;
    }

    function validateForm() {
        let isValid = true;
        inputs.each(function() {
            if (!validateField($(this))) {
                isValid = false;
            }
        });
        return isValid;
    }

    function updateFieldStatus(field, isValid, message) {
        const feedback = field.siblings('.feedback');
        if (!feedback.length) {
            field.after('<div class="feedback"></div>');
        }
        
        if (!isValid) {
            field.addClass('error').removeClass('success');
            field.siblings('.feedback').addClass('error').text(message);
        } else {
            field.addClass('success').removeClass('error');
            field.siblings('.feedback').removeClass('error').text('');
        }
    }

    function checkPasswordStrength(password) {
        let strength = 0;
        if (password.length >= 8) strength++;
        if (password.match(/[A-Z]/)) strength++;
        if (password.match(/[0-9]/)) strength++;
        if (password.match(/[^A-Za-z0-9]/)) strength++;
        return strength;
    }

    function updatePasswordStrength(strength) {
        const strengthBar = $('.password-strength');
        if (!strengthBar.length) {
            passwordInput.after('<div class="password-strength"><div class="strength-bar"></div></div>');
        }
        
        const bar = $('.strength-bar');
        const percentage = (strength / 4) * 100;
        bar.css('width', `${percentage}%`);
        
        const colors = ['#ff4444', '#ffbb33', '#00C851', '#007E33'];
        bar.css('background-color', colors[strength - 1] || '#ff4444');
    }

    // Add this new code for login link
    $('.login-link a').on('click', function(e) {
        e.preventDefault();
        window.location.href = './login.html';
    });
}); 