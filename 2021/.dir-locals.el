;;; Directory Local Variables
;;; For more information see (info "(emacs) Directory Variables")

((python-mode . ((pyvenv-activate . "../.venv")
                 (eval . (progn
                           (load-file (concat (locate-dominating-file default-directory dir-locals-file) "gcj.el"))
                           (gcj-mode))))))
