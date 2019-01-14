(require 'find-lisp)

(defun indent-file (file-name)
  (save-window-excursion
    (find-file file-name)
    (indent-region (point-min) (point-max))
    (write-region nil nil file-name)))


(mapc 'indent-file (find-lisp-find-files (elt argv 0) "\\.html$"))
