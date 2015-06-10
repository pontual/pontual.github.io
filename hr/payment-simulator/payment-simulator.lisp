(defvar *bills* '(100 50 20 10 5 2 1))

(defun inc-bill-count (bill bill-counts)
  (labels ((iter (bill bill-counts new-bill-counts)
             (cond ((null bill-counts) new-bill-counts)
                   ((= bill (car bill-counts))
                    (iter bill (cddr bill-counts) (cons bill (cons (+ 1 (cadr bill-counts)) new-bill-counts))))
                   (t (iter bill (cddr bill-counts) (cons (car bill-counts) (cons (cadr bill-counts) new-bill-counts)))))))
    (iter bill bill-counts '())))

(defun inc-bill-count-rec (bill bill-counts)
  (if (null bill-counts)
      '()
      (let ((bill-counts-denom (car bill-counts))
            (bill-counts-count (cadr bill-counts)))
        (cons bill-counts-denom
              (cons
               (if (= bill bill-counts-denom)
                   (+ 1 bill-counts-count)
                   bill-counts-count)
               (inc-bill-count-rec bill (cddr bill-counts)))))))

(defun copy (lst)
  (if (null lst)
      '()
      (cons (car lst) (copy (cdr lst)))))

(defun bad-copy (lst)
  (if (null lst)
      '()
      (bad-copy (cdr lst))))

(defun count-for-payment (payment bills)
  (labels ((iter (payment bills bill-counts)
             (cond ((= payment 0) bill-counts)
                   ((null bills) payment) ;(error "Ran out of bill denominations"))
                   (t (let ((bill-denom (car bills)))
                        (if (>= payment bill-denom)
                            (iter (- payment bill-denom)
                                  bills
                                  (inc-bill-count-rec bill-denom bill-counts))
                            (iter payment (cdr bills) bill-counts)))))))
    (iter payment bills (empty-counts bills))))

(defun empty-counts (bills)
  (if (null bills)
      '()
      (cons (car bills) (cons 0 (empty-counts (cdr bills))))))

(defun pick-count (denom counts)
  (if (= denom (car counts))
      (cadr counts)
      (pick-count denom (cddr counts))))

(defun accum-denom (denom n)
  (let ((totals '()))
    (dotimes (i n)
      (let ((payment (+ 100 (random 1000))))
        (push (pick-count denom (count-for-payment payment *bills*)) totals)))
    ;; (push payment totals)))
    totals))

(defun sum-denom (denom n)
  (apply #'+ (accum-denom denom n)))

(defun repeat-group (denom num-payments n)
  (let ((group-totals '()))
    (dotimes (i n)
      (push (sum-denom denom num-payments) group-totals))
    group-totals))

(defun get-percentiles (bills payments repetitions percentile)
  (let ((percentiles '()))
    (dolist (denom bills)
      (push (nth (round (* (/ percentile 100) repetitions))
                 (sort (repeat-group denom payments repetitions)
                       #'<))
            percentiles)
      (push (write-to-string denom) percentiles))
    percentiles))

;;; 29 people (22 + 7 (vale-tr)), random (100 to 1099), 90th percentile
(get-percentiles *bills* 29 1000 90)
