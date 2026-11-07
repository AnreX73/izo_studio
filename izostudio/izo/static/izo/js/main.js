!function(e){"function"!=typeof e.matches&&(e.matches=e.msMatchesSelector||e.mozMatchesSelector||e.webkitMatchesSelector||function(e){for(var t=this,o=(t.document||t.ownerDocument).querySelectorAll(e),n=0;o[n]&&o[n]!==t;)++n;return Boolean(o[n])}),"function"!=typeof e.closest&&(e.closest=function(e){for(var t=this;t&&1===t.nodeType;){if(t.matches(e))return t;t=t.parentNode}return null})}(window.Element.prototype);

document.addEventListener('DOMContentLoaded', function() {
    var modalButtons = document.querySelectorAll('.js-open-modal'),
    overlay      = document.querySelector('#overlay-modal'),
    closeButtons = document.querySelectorAll('.js-modal-close');
    

    modalButtons.forEach(function(item){
        item.addEventListener('click', function(e) {
            e.preventDefault();
            var modalId = this.getAttribute('data'); 
            modalElem = document.querySelector('.modal[data="' + modalId + '"]');
            modalElem.classList.add('active');
            overlay.classList.add('active');

        });

    });
    closeButtons.forEach(function(item){

        item.addEventListener('click', function(e) {
           var parentModal = this.closest('.modal');
           parentModal.classList.remove('active');
           overlay.classList.remove('active');
        });
     
     });
     document.body.addEventListener('keyup', function (e) {
        var key = e.keyCode;
    
        if (key == 27) {
            document.querySelector('.modal.active').classList.remove('active');
            document.querySelector('.overlay.active').classList.remove('active');
        };
    }, false);

    overlay.addEventListener('click', function() {
        document.querySelector('.modal.active').classList.remove('active');
        this.classList.remove('active');
    });

});

/* модальное окно для новости */
document.addEventListener('DOMContentLoaded', function() {
    overlay      = document.querySelector('#post-overlay-modal'),
    closeButton = document.querySelector('.post-modal__cross');
    modalElem = document.querySelector('.post-modal');
    checkElem = sessionStorage.getItem("cookie-message");
    if (checkElem == undefined) {
        setTimeout(function(){
            modalElem.classList.add('active');
            overlay.classList.add('active');;
        },500)
        
      }
    

    closeButton.addEventListener('click', function(e) {
        var parentModal = this.closest('.post-modal');
         sessionStorage.setItem("cookie-message", true);
         parentModal.classList.remove('active');
         overlay.classList.remove('active');
         
      });

       /* закрытие по ESC */
  document.body.addEventListener('keyup', function (e) {
    var key = e.keyCode;
    if (key == 27) {
        sessionStorage.setItem("cookie-message", true);
        document.querySelector('.post-modal.active').classList.remove('active');
        document.querySelector('.post-overlay.active').classList.remove('active');
    };
  }, false);
    /* скрытие окна при клике на подложку */
    overlay.addEventListener('click', function() {
        sessionStorage.setItem("cookie-message", true);
        document.querySelector('.post-modal.active').classList.remove('active');
        this.classList.remove('active');
      });

});

/* Переключатель светлой и тёмной темы */
(function () {
    var root = document.documentElement;
    var toggle = document.getElementById('theme-toggle');
    var meta = document.querySelector('meta[name="theme-color"]');
    var storageKey = 'izo-theme';

    function getTheme() {
        return root.getAttribute('data-theme') === 'dark' ? 'dark' : 'light';
    }

    function updateToggle(theme) {
        if (!toggle) return;
        var isDark = theme === 'dark';
        toggle.setAttribute('aria-checked', isDark ? 'true' : 'false');
        toggle.setAttribute('aria-label', isDark
            ? 'Переключить на светлую тему'
            : 'Переключить на тёмную тему');
        toggle.setAttribute('title', isDark ? 'Светлая тема' : 'Тёмная тема');
    }

    function applyTheme(theme, persist) {
        root.setAttribute('data-theme', theme);
        if (meta) {
            meta.setAttribute('content', theme === 'dark' ? '#101216' : '#fafafa');
        }
        updateToggle(theme);
        if (persist) {
            try {
                localStorage.setItem(storageKey, theme);
            } catch (e) {}
        }
    }

    applyTheme(getTheme(), false);

    if (toggle) {
        toggle.addEventListener('click', function () {
            applyTheme(getTheme() === 'dark' ? 'light' : 'dark', true);
        });
    }

    /* Следим за системной темой, пока пользователь не выбрал свою */
    if (window.matchMedia) {
        var media = window.matchMedia('(prefers-color-scheme: dark)');
        var onSystemChange = function (event) {
            var saved = null;
            try {
                saved = localStorage.getItem(storageKey);
            } catch (e) {}
            if (saved === 'dark' || saved === 'light') return;
            applyTheme(event.matches ? 'dark' : 'light', false);
        };
        if (typeof media.addEventListener === 'function') {
            media.addEventListener('change', onSystemChange);
        } else if (typeof media.addListener === 'function') {
            media.addListener(onSystemChange);
        }
    }
})();