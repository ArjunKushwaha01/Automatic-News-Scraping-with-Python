/* styles.css */

/* Base */
body {
  font-family: 'Roboto', sans-serif;
  background-color: #f8f9fa;
  color: #212529;
  transition: background-color 0.3s, color 0.3s;
  min-height: 100vh;
}

/* Dark Mode */
.dark-mode body {
  background-color: #121212;
  color: #f8f9fa;
}

/* Navbar */
.navbar-custom {
  background: linear-gradient(135deg, #1d3557, #457b9d);
  box-shadow: 0 4px 8px rgb(29 53 87 / 0.4);
}

.navbar-brand {
  color: #fff !important;
  font-weight: 700;
  font-size: 1.75rem;
  transition: color 0.3s ease;
}

.navbar-brand:hover {
  color: #a8dadc !important;
}

.nav-link {
  color: #e0e0e0 !important;
  font-weight: 500;
  transition: color 0.3s ease;
}

.nav-link:hover {
  color: #f1faee !important;
}

.nav-link.active {
  font-weight: 700;
  color: #f1faee !important;
  text-decoration: underline;
}

/* Sidebar */
.sidebar {
  background-color: #f8f9fa;
  border-right: 1px solid #dee2e6;
  padding-top: 1rem;
  height: 100vh;
  position: sticky;
  top: 0;
  overflow-y: auto;
  box-shadow: inset -1px 0 0 rgb(0 0 0 / 0.1);
  transition: background-color 0.3s;
}

.dark-mode .sidebar {
  background-color: #1f1f1f;
  border-color: #333;
  box-shadow: inset -1px 0 0 rgb(255 255 255 / 0.1);
}

.sidebar h5 {
  color: #1d3557;
  font-weight: 700;
  margin-bottom: 1rem;
}

.dark-mode .sidebar h5 {
  color: #a8dadc;
}

.sidebar .nav-link {
  color: #495057;
  padding: 0.5rem 1rem;
  font-weight: 600;
  border-radius: 0.375rem;
  margin-bottom: 0.25rem;
  transition: background-color 0.3s, color 0.3s;
}

.sidebar .nav-link:hover {
  background-color: #e9ecef;
  color: #1d3557;
}

.sidebar .nav-link.active {
  background-color: #457b9d;
  color: white !important;
  font-weight: 700;
}

.dark-mode .sidebar .nav-link {
  color: #cfd8dc;
}

.dark-mode .sidebar .nav-link:hover {
  background-color: #2a2a2a;
  color: #a8dadc;
}

.dark-mode .sidebar .nav-link.active {
  background-color: #1d3557;
  color: #a8dadc !important;
}

/* Cards */
.news-card {
  background-color: white;
  border-radius: 15px;
  box-shadow: 0 6px 15px rgb(0 0 0 / 0.1);
  transition: transform 0.25s ease, box-shadow 0.25s ease;
  overflow: hidden;
  margin-bottom: 1.5rem;
}

.news-card:hover {
  transform: scale(1.03);
  box-shadow: 0 12px 30px rgb(0 0 0 / 0.15);
}

.dark-mode .news-card {
  background-color: #2c2c2c;
  color: #f8f9fa;
  box-shadow: 0 6px 15px rgb(255 255 255 / 0.1);
}

.dark-mode .news-card:hover {
  box-shadow: 0 12px 30px rgb(255 255 255 / 0.15);
}

/* Card Text */
.card-title {
  font-size: 1.4rem;
  font-weight: 700;
  margin-bottom: 0.5rem;
  color: inherit;
}

.card-subtitle {
  font-size: 0.9rem;
  color: #6c757d;
  margin-bottom: 1rem;
}

.dark-mode .card-subtitle {
  color: #adb5bd;
}

.card-text {
  max-height: 120px;
  overflow: hidden;
  text-overflow: ellipsis;
  color: inherit;
}

/* Fade animations */
.fade-out {
  opacity: 0;
  transition: opacity 0.5s ease-out;
}

#page-content {
  animation: fadeIn 0.5s ease-in;
}

@keyframes fadeIn {
  from { opacity: 0; }
  to { opacity: 1; }
}

/* Dark mode toggle cursor */
.dark-toggle {
  cursor: pointer;
  font-size: 1.25rem;
  user-select: none;
  transition: color 0.3s ease;
}

.dark-toggle:hover {
  color: #a8dadc;
}

/* Responsive fixes */
@media (max-width: 767.98px) {
  .sidebar {
    display: none;
  }
}

/* Scrollbar for sidebar */
.sidebar::-webkit-scrollbar {
  width: 8px;
}

.sidebar::-webkit-scrollbar-thumb {
  background-color: rgba(0, 0, 0, 0.1);
  border-radius: 4px;
}

.dark-mode .sidebar::-webkit-scrollbar-thumb {
  background-color: rgba(255, 255, 255, 0.15);
}
