;; Fizzbuzz written in Emacs Lisp
;;
;;
;;

(defun fizzbuzz (num)
  "function demonstrating fizzbuzz in emacs lisp"
  (interactive "p")
  (while (< num 101)
    (cond 
     ((and (= (mod num 3) 0) (= (mod num 5) 0)) (princ "FIzzbuZZ"))
     ((= (mod num 3) 0) (princ "fizz"))
     ((= (mod num 5) 0) (princ "buzz"))
     ((princ num)))
    (setq num (1+ num))))
  
