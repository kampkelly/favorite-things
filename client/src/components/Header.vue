<template>
    <div>
        <header>
            <nav class="">
                <div>
                    <h2>Favorite Things</h2>
                </div>
                <div>
                    <i class="fas fa-ellipsis-v"></i>
                </div>
            </nav>
        </header>
    </div>
</template>

<script>
export default {

};
</script>

<style lang="scss" scoped>
 header {
     nav {
         margin: 0px;
         background: #6202EE;
         display: flex;
         padding: 0em 1em 0em 1em;
         > div:nth-child(1) {
             flex: 5;
             h2 {
                 text-align: center;
             }
         }
         > div:nth-child(2) {
             flex: 1;
             text-align: right;
             i {
                 font-size: 1.5em;
                 padding-top: 20px;
             }
         }
     }
 }
</style>
