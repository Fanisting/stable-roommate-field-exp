clear all
cd "E:\OneDrive - zju.edu.cn\Field_with_Wenyuan\stable-roommates\class"

foreach x of numlist 115/123 {
	clear all
	import excel "`x'.xlsx", sheet("Sheet1") firstrow
	save "temp_`x'.dta", replace
	clear
	import excel "names.xlsx", sheet("Sheet1") firstrow
	keep if class == `x'
	merge 1:1 name using "temp_`x'.dta"
	keep name class gender self_piece win_tour _merge
	erase "temp_`x'.dta"
	export excel using "`x'_merge.xlsx", firstrow(variables) replace
}