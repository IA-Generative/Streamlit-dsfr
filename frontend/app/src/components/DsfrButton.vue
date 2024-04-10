<script setup lang="ts">
import { onMounted, onUnmounted, ref, computed } from 'vue'
import { Streamlit } from '~/stcomponentlib'

import '~/assets/iconify-icon.min.js'

import { useStreamlit } from '~/streamlit'
import type { ComponentProps } from '~/types/ComponentProps.d.ts'
import DsfrButton from '~/components/dsfr/DsfrButton.vue'

useStreamlit()

const props = defineProps<
	ComponentProps<{
		label?: string
		secondary?: boolean
		tertiary?: boolean
		disabled?: boolean
		icon?: string
		iconOnly?: boolean
		iconRight?: boolean
		noOutline?: boolean
		size?: '' | 'small' | 'sm' | 'lg' | 'large' | 'md' | 'medium'
		// Custom props
		link?: string
		copy?: string
	}>
>()

const clicked = ref<boolean>(false)

let toggleOffTimeout: number | undefined = undefined
let lockTimeout: number | undefined = undefined

function onRenderEvent(_event: Event): void
{
	if (
		clicked.value &&
		lockTimeout === undefined
	)
	{
		clicked.value = false
		Streamlit.setComponentValue(clicked.value)
	}
}

onMounted(() =>
	{
		Streamlit.events.addEventListener(Streamlit.RENDER_EVENT, onRenderEvent)
	})

onUnmounted(() =>
	{
		Streamlit.events.removeEventListener(Streamlit.RENDER_EVENT, onRenderEvent)
	})

async function onClick()
{
	if (clicked.value)
	{
		clicked.value = false
		Streamlit.setComponentValue(clicked.value)

		await new Promise(resolve => setTimeout(resolve, 50))
	}

	clicked.value = true
	Streamlit.setComponentValue(clicked.value)

	if (toggleOffTimeout)
	{
		clearTimeout(toggleOffTimeout)
	}

	if (lockTimeout)
	{
		clearTimeout(lockTimeout)
	}

	lockTimeout = -1
	toggleOffTimeout = setTimeout(() =>
		{
			clicked.value = false
			Streamlit.setComponentValue(clicked.value)

			lockTimeout = setTimeout(() =>
				{
					lockTimeout = undefined
				}, 50)

			toggleOffTimeout = undefined
		}, 50)
}
</script>

<template>
	<div class="component" :style="style">
		<DsfrButton
			v-bind="props.args"
			:disabled="clicked || props.disabled || props.args.disabled"
			@click="onClick"
		/>
	</div>
</template>
