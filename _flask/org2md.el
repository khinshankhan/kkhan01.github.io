(require 'find-lisp)

(require 'org)
(eval-after-load "org"
  '(load (concat user-emacs-directory "elpa/ox-gfm-20170628.2102/ox-gfm.el")))

(defun org2md (file-name)
  (save-window-excursion
    (find-file file-name)
    (org-gfm-export-to-markdown)))

(mapc 'org2md (find-lisp-find-files (elt argv 0) "\\.org$"))
