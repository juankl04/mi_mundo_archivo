     (galeria {
    display: flex;
    width: 500px;
    height: 300px;
}galeria img {
    width: 0px
    flex-grow: 1;
    object-fit:cover ;
    filter : brightness(80%);
    transition: .7s ease;
}
.galeria img:hover{
    widht: 500px;
    opacity: 1;
    filter: brightness(130%);
}
