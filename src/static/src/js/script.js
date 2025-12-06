// Handle dropdown submenus
document.addEventListener('DOMContentLoaded', function() {
    const dropdownItems = document.querySelectorAll('.dropdown-submenu > a');
    
    dropdownItems.forEach(item => {
        item.addEventListener('click', function(e) {
            e.preventDefault();
            e.stopPropagation();
            
            // Close all other submenus
            document.querySelectorAll('.dropdown-submenu .dropdown-menu').forEach(menu => {
                if (menu !== this.nextElementSibling) {
                    menu.classList.remove('show');
                }
            });
            
            // Toggle current submenu
            const submenu = this.nextElementSibling;
            submenu.classList.toggle('show');
        });
    });
    
    // Close submenus when clicking outside
    document.addEventListener('click', function(e) {
        if (!e.target.closest('.dropdown-submenu')) {
            document.querySelectorAll('.dropdown-submenu .dropdown-menu').forEach(menu => {
                menu.classList.remove('show');
            });
        }
    });
});

class BackToTop {
    constructor() {
        this.button = document.getElementById('backToTop');
        this.threshold = 300;
        this.init();
    }
    
    init() {
        this.addScrollListener();
        this.addClickListener();
    }
    
    addScrollListener() {
        window.addEventListener('scroll', () => {
            this.toggleVisibility();
        });
        
        // Проверяем начальную позицию
        this.toggleVisibility();
    }
    
    addClickListener() {
        this.button.addEventListener('click', (e) => {
            e.preventDefault();
            this.scrollToTop();
        });
    }
    
    toggleVisibility() {
        if (window.pageYOffset > this.threshold) {
            this.button.classList.add('show');
        } else {
            this.button.classList.remove('show');
        }
    }
    
    scrollToTop() {
        window.scrollTo({
            top: 0,
            behavior: 'smooth'
        });
    }
}

// Инициализация когда DOM загружен
document.addEventListener('DOMContentLoaded', () => {
    new BackToTop();
});


