html_folder <- "~/florian/Dropbox/Fac/ENSG_L3PRO/Cours" 

pdf_output_folder <- "florian/Dropbox/fac/ENSG_L3PRO/Cours/pdf/"

html_files <- list.files(path = html_folder, pattern = "*.html", full.names = TRUE)

for (html_file in html_files) {
  print(html_file)
  
  pdf_file <- gsub(".html", ".pdf", basename(html_file))  
  pdf_file <- file.path(pdf_output_folder, pdf_file)  
  
  system(paste("pandoc", shQuote(html_file), "--pdf-engine=wkhtmltopdf", "-o", shQuote(pdf_file)))
}

