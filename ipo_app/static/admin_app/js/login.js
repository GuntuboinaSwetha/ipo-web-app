// $(document).ready(function() {
//     const form = $('form');
//     const inputs = $('input[type="email"], input[type="password"]');
//     const passwordInput = $('#password');
//     const togglePassword = $('#togglePassword');
//     const submitButton = $('.signup-button');

//     // Show/Hide password
//     togglePassword.on('click', function() {
//         const type = passwordInput.attr('type') === 'password' ? 'text' : 'password';
//         passwordInput.attr('type', type);
//         $(this).toggleClass('fa-eye fa-eye-slash');
//     });

//     // Real-time validation
//     inputs.on('blur', function() {
//         validateField($(this));
//     });

//     // Form submission
//     form.on('submit', function(e) {
//         e.preventDefault();
        
//         if (validateForm()) {
//             // Verify reCAPTCHA
//             const recaptchaResponse = grecaptcha.getResponse();
//             if (!recaptchaResponse) {
//                 Swal.fire({
//                     icon: 'error',
//                     title: 'Verification Required',
//                     text: 'Please complete the reCAPTCHA verification'
//                 });
//                 return;
//             }

//             const formData = {
//                 email: $('#email').val(),
//                 password: $('#password').val(),
//                 remember: $('input[name="remember"]').is(':checked'),
//                 recaptchaResponse: recaptchaResponse
//             };

//             submitButton.prop('disabled', true).html('<span class="spinner"></span> Logging in...');

//             // Simulate API call
//             setTimeout(() => {
//                 $.ajax({
//                     url: '/api/login',
//                     method: 'POST',
//                     data: formData,
//                     success: function(response) {
//                         Swal.fire({
//                             icon: 'success',
//                             title: 'Success!',
//                             text: 'Login successful!',
//                             showConfirmButton: false,
//                             timer: 1500
//                         }).then(() => {
//                             window.location.href = '/dashboard';
//                         });
//                     },
//                     error: function(xhr) {
//                         const error = xhr.responseJSON?.message || 'Invalid email or password';
//                         Swal.fire({
//                             icon: 'error',
//                             title: 'Login Failed',
//                             text: error
//                         });
//                         submitButton.prop('disabled', false).text('Log in');
//                     }
//                 });
//             }, 1000);
//         }
//     });

//     // Validation functions
//     function validateField(field) {
//         const value = field.val();
//         const name = field.attr('name');
//         let isValid = true;
//         let message = '';

//         switch(name) {
//             case 'email':
//                 const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
//                 if (!emailRegex.test(value)) {
//                     isValid = false;
//                     message = 'Please enter a valid email address';
//                 }
//                 break;
//             case 'password':
//                 if (value.length < 1) {
//                     isValid = false;
//                     message = 'Password is required';
//                 }
//                 break;
//         }

//         updateFieldStatus(field, isValid, message);
//         return isValid;
//     }

//     function validateForm() {
//         let isValid = true;
//         inputs.each(function() {
//             if (!validateField($(this))) {
//                 isValid = false;
//             }
//         });
//         return isValid;
//     }

//     function updateFieldStatus(field, isValid, message) {
//         const feedback = field.siblings('.feedback');
//         if (!feedback.length) {
//             field.after('<div class="feedback"></div>');
//         }
        
//         if (!isValid) {
//             field.addClass('error').removeClass('success');
//             field.siblings('.feedback').addClass('error').text(message);
//         } else {
//             field.addClass('success').removeClass('error');
//             field.siblings('.feedback').removeClass('error').text('');
//         }
//     }

//     // Sign up link handler
//     $('.create-account a').on('click', function(e) {
//         e.preventDefault();
//         window.location.href = './signup.html';
//     });

//     // Forgot password link handler
//     $('.forgot-password').on('click', function(e) {
//         e.preventDefault();
//         window.location.href = './forgot-password.html';
//     });
// });

// // Add this after your document ready function
// window.onRecaptchaError = function() {
//     Swal.fire({
//         icon: 'error',
//         title: 'reCAPTCHA Error',
//         text: 'Failed to load reCAPTCHA. Please refresh the page and try again.',
//         confirmButtonColor: '#6366f1'
//     });
// }; 