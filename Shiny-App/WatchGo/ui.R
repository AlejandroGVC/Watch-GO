# UIHeader ----
header <- dashboardHeader(
    title = "Watch&Go"
    )
# UIBody ----
body <- dashboardBody(
    # Tab Búsqueda ----
    tabItem(tabName = 'Búsqueda',
            fluidRow(
                box(title = 'Busca tu pelicula',
                    id = 'buscador',
                    width = 4,
                    height = '100px',
                    align = 'center',
                    searchInput(
                        inputId = "search",
                        label = "Introduce una pelicula", 
                        placeholder = "Ejemplo: Avengers",
                        btnSearch = icon("search"), 
                        btnReset = icon("remove"),
                        width = "100%"
                    )
                )
            )
        )
)
