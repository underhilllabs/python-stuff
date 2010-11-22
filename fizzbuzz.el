;;(setq num 1)
;;(if (and (< (mod num 3) 1) (< (mod num 5) 1)) (princ "fizzbuzz"))
;;(1+ num)
;;(princ num)

(defun fizzbuzz (num)
  (princ num)
  (if (< num 100)
      (cond 
       ((and (< (mod num 3) 1) (< (mod num 5) 1)) (princ "fizzbuzz"))
       ((< (mod num 5) 1) (princ "fizz"))
       ((< (mod num 3) 1) (princ "buzz"))
       ((princ num)))
      (setq num (+ num 1))
      (fizzbuzz num))
  (princ '("nothin doin" num)))
(fizzbuzz 11)



(defun fizzbuzz (num)
  (cond 
   ((and (< (mod num 3) 1) (< (mod num 5) 1)) (princ "fizzbuzz"))
   ((< (mod num 5) 1) (princ "fizz"))
   ((< (mod num 3) 1) (princ "buzz"))
   ((princ num)))
  )
(setq numb 1)
(while (< numb 100) ((fizzbuzz numb)(setq numb (+1 numb)))) 

(defun fizzbuzzl (num)
  (
   (cond 
   ((and (< (mod num 3) 1) (< (mod num 5) 1)) (princ "fizzbuzz"))
   ((< (mod num 5) 1) (princ "fizz"))
   ((< (mod num 3) 1) (princ "buzz"))
   ((princ num)))
   (setq num (+1 num)) 
   (fizzbuzzl num)
  )
)
(fizzbuzzl 1)