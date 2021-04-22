;;; gcj.el --- Minor mode to easily run Google Code Jam problems

;;; Commentary:

;; Run Google Code Jam problems.

;;; Code:

(defcustom gcj-run-command "python %1$s.py < %1$s.in"
  "The command to run when solving a Google Code Jam problem."
  :type 'string
  :group 'programming)

(defun gcj-run ()
  "Run a google code jam problem."
  (interactive)
  (let ((problem (file-name-sans-extension (buffer-name))))
    (compile (format gcj-run-command problem))))

(define-minor-mode gcj-mode
  "Toggle global gcj-mode."
  nil
  :global t
  :group 'programming
  :lighter " gcj"
  :keymap
  (list (cons (kbd "C-c r") #'gcj-run)))

(provide 'gcj)
;;; gcj.el ends here
