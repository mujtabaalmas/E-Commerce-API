# 🛒 E-Commerce Web Application – Django Backend API

## 🚀 Backend: Django + Django REST Framework  
## 🧪 API Testing: Postman  

---

## ✅ Features & Functionality

This backend supports session-based customer operations and user-based (vendor/admin) operations.

---

## 👥 CUSTOMER FUNCTIONALITY

- 🔍 **View Products**  
  `GET http://localhost:PORT/api/products/`  
  *(Session ID is auto-created via cookies.)*

- ➕ **Add to Cart**  
  `POST http://localhost:PORT/api/cart/cart/add/`

- 🛒 **View Cart**  
  `GET http://localhost:PORT/api/cart/cart/`

- 💳 **Checkout (Name & Email Required)**  
  `POST http://localhost:PORT/api/orders/checkout/`

---

## 👤 USER FUNCTIONALITY

- 📝 **Register**  
  `POST http://localhost:8000/api/users/register/`

- 🔐 **Login**  
  `POST http://localhost:PORT/api/users/login/`

- 🚪 **Logout**  
  `POST http://localhost:PORT/api/users/logout/`

- 🧾 **View Vendors (After Login)**  
  `GET http://localhost:PORT/api/vendors/` *(Assuming this endpoint)*

---

## ⚙️ Notes

- Replace `PORT` with your actual server port (e.g., `8000`).
- Use **Postman** with cookie handling enabled for session-based customer actions.
- Vendor routes require authentication.
- All endpoints follow RESTful conventions.
