<script setup lang="ts">
import StreamlitComponent from '~/components/StreamlitComponent.vue'
import Component from '~/components/DsfrFileUpload.vue'
</script>

<template>
	<StreamlitComponent :component="Component" client:load />
</template>
