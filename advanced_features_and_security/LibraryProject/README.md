## Permissions and Groups Setup
- **Groups created**: Admins, Editors, Viewers.
- **Viewers**: Can use `can_view` permission.
- **Editors**: Can use `can_view`, `can_create`, and `can_edit`.
- **Admins**: Can use all permissions including `can_delete`.
 
 
 # Security Implementation and Permissions Guide

## 1. Secure Settings (settings.py)
The following security configurations have been implemented to protect the application in a production environment:
- **DEBUG = False**: Prevents sensitive error traces from being exposed to users.
- **Browser Protection Headers**: 
    - `SECURE_BROWSER_XSS_FILTER` is enabled to activate the browser's XSS filtering.
    - `X_FRAME_OPTIONS = 'DENY'` prevents clickjacking attacks by forbidding the site from being framed.
    - `SECURE_CONTENT_TYPE_NOSNIFF` prevents the browser from guessing content types, reducing XSS risks.
- **Cookie Security**: `CSRF_COOKIE_SECURE` and `SESSION_COOKIE_SECURE` are set to `True` to ensure cookies are only transmitted over HTTPS.

## 2. CSRF Protection
All forms within the application, such as those in `form_example.html`, explicitly include the `{% csrf_token %}` tag to prevent Cross-Site Request Forgery attacks.

## 3. SQL Injection Protection
All data access in `views.py` is handled through the **Django ORM**. We avoid raw SQL queries and string formatting for user inputs, utilizing parameterized queries provided by the ORM to ensure safety.

## 4. Custom Permissions and Groups
- **Models**: The `Book` model includes custom permissions: `can_view`, `can_create`, `can_edit`, and `can_delete`.
- **Groups**:
    - **Viewers**: Assigned `can_view`.
    - **Editors**: Assigned `can_view`, `can_create`, and `can_edit`.
    - **Admins**: Assigned all four permissions.
- **Enforcement**: Views are protected using the `@permission_required` decorator.