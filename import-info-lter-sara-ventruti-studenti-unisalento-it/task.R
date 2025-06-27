setwd('/app')
library(optparse)
library(jsonlite)




print('option_list')
option_list = list(

make_option(c("--url"), action="store", default=NA, type="character", help="my description"),
make_option(c("--id"), action="store", default=NA, type="character", help="task id")
)


opt = parse_args(OptionParser(option_list=option_list))

var_serialization <- function(var){
    if (is.null(var)){
        print("Variable is null")
        exit(1)
    }
    tryCatch(
        {
            var <- fromJSON(var)
            print("Variable deserialized")
            return(var)
        },
        error=function(e) {
            print("Error while deserializing the variable")
            print(var)
            var <- gsub("'", '"', var)
            var <- fromJSON(var)
            print("Variable deserialized")
            return(var)
        },
        warning=function(w) {
            print("Warning while deserializing the variable")
            var <- gsub("'", '"', var)
            var <- fromJSON(var)
            print("Variable deserialized")
            return(var)
        }
    )
}

print("Retrieving url")
var = opt$url
print(var)
var_len = length(var)
print(paste("Variable url has length", var_len))

url <- gsub("\"", "", opt$url)
id <- gsub('"', '', opt$id)


print("Running the cell")
url
data_vec = 1 + url
# capturing outputs
print('Serialization of data_vec')
file <- file(paste0('/tmp/data_vec_', id, '.json'))
writeLines(toJSON(data_vec, auto_unbox=TRUE), file)
close(file)
